from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import move_counters_ability
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack


_move_counters, _can_move = move_counters_ability(3, "theirs")

card = PokemonCardDef(
    guid="a2725c13-fa3b-54f0-8715-c98548ae5859",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name",
    display_name="Absol",
    searchable_by=["Absol", "Basic", "Absol"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="XY6",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=359,
    abilities=[
        Ability(
            title="Cursed Eyes",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may move 3 damage counters from 1 of your opponent's Pok\u00e9mon to another of his or her Pok\u00e9mon.",
            trigger=Triggers.ON_PLAY,
            effect=_move_counters,
        ),
        Attack(
            title="Mach Claw",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ignore_modifier_attack(ignore_resistance=True),
        ),
    ],
)