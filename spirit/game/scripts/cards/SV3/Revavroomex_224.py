from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="48b80dab-e832-5c08-b22a-d0f1920622f4",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Revavroomex.Name",
    display_name="Revavroom ex",
    searchable_by=["Revavroom ex", "Stage 1", "ex", "Revavroomex"],
    subtypes=["Stage 1", "ex"],
    collector_number=224,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    family_id=965,
    abilities=[
        Ability(
            title="Tune-Up",
            game_text="This Pok\u00e9mon may have up to 4 Pok\u00e9mon Tools attached to it. If it loses this Ability, discard Pok\u00e9mon Tools from it until only 1 remains.",
            effect=unimplemented,
        ),
        Attack(
            title="Wild Drift",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=unimplemented,
        ),
    ],
)