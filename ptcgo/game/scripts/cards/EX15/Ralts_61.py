from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b561b029-c233-5146-8c78-55773466a431",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    display_name="Ralts δ",
    searchable_by=["Ralts \u03b4", "Basic", "Ralts"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=280,
    abilities=[
        Attack(
            title="Calm Mind",
            game_text="Remove 2 damage counters from Ralts.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Will-o'-the-wisp",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)