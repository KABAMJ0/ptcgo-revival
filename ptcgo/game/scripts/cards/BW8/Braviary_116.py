from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per
from ptcgo.game.card_effects.attacks_common import optional_bonus_self_damage


card = PokemonCardDef(
    guid="2b4d114d-a723-5e1b-9d91-e67d56199a7c",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Braviary.Name",
    display_name="Braviary",
    searchable_by=["Braviary", "Stage 1", "Braviary"],
    subtypes=["Stage 1"],
    collector_number=116,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    family_id=627,
    abilities=[
        Ability(
            title="Big Wing",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=lambda board, player_id, pokemon: is_in_active_spot(pokemon),
            effect=gust_attack(damage_before=0, opponent_chooses=True),
        ),
        Attack(
            title="Wild Edge",
            game_text="You may do 20 more damage. If you do, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=optional_bonus_self_damage(20, 20),
        ),
    ],
)