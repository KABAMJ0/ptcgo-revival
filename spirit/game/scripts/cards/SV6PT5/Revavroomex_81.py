from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2069fdaa-5f01-5b82-bd8b-f7de4a90689f",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Revavroomex.Name",
    display_name="Revavroom ex",
    searchable_by=["Revavroom ex", "Stage 1", "Tera", "ex", "Revavroomex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=81,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    family_id=965,
    abilities=[
        Attack(
            title="Accelerator Flash",
            game_text="If this Pok\u00e9mon moved from your Bench to the Active Spot this turn, this attack does 120 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Shattering Speed",
            game_text="Discard this Pok\u00e9mon and all attached cards.",
            cost={PokemonTypes.METAL: 3},
            damage=250,
            effect=unimplemented,
        ),
    ],
)