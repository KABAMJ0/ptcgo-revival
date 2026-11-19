from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_pokemon_ex
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
card = PokemonCardDef(
    guid="2106f4c0-6354-5c3a-b801-31d893995379",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoopaEX.Name",
    display_name="Hoopa-EX",
    searchable_by=["Hoopa-EX", "Basic", "EX", "HoopaEX"],
    subtypes=["Basic", "EX"],
    collector_number=36,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=720,
    abilities=[
        Ability(
            title="Scoundrel Ring",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may search your deck for up to 3 Pok\u00e9mon-EX (except for Hoopa-EX), reveal them, and put them into your hand. Shuffle your deck afterward.",
            trigger=Triggers.ON_PLAY,
            effect=search_to_hand(is_pokemon_ex, count=3, reveal=True),
        ),
        Attack(
            title="Hyperspace Fury",
            game_text="Discard 2 Energy attached to this Pok\u00e9mon. This attack does 100 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=self_energy_discard_attack(count=2, before_damage=True, also=snipe_attack(100, pool="any", count=1)),
        ),
    ],
)