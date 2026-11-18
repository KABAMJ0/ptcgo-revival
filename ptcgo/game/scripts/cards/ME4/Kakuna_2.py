from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5c75fea5-66d4-5aad-ac73-e2a932269f15",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    display_name="Kakuna",
    searchable_by=["Kakuna", "Stage 1", "Kakuna"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="ME4",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    family_id=13,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="This Pok\u00e9mon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Hang Down",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)