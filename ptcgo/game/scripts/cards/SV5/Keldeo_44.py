from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9100f7d9-4a9a-5b55-acc3-b3f5141dff8a",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Keldeo.Name",
    display_name="Keldeo",
    searchable_by=["Keldeo", "Basic", "Keldeo"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=647,
    abilities=[
        Attack(
            title="Rapid Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Aqua Blade",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)