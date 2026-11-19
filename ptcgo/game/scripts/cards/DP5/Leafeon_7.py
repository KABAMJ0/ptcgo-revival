from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="838d18ab-e487-5ce1-ae60-6e4afa234617",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name",
    display_name="Leafeon",
    searchable_by=["Leafeon", "Stage 1", "Leafeon"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="DP5",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Bind Down",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Leaf Guard",
            game_text="During your opponent's next turn, any damage done to Leafeon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=protect_next_turn(reduce=20),
        ),
    ],
)