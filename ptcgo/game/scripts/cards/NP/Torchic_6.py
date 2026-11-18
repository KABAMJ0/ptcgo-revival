from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b1c23d87-f336-5063-8c16-cf298046cd0c",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    display_name="Torchic",
    searchable_by=["Torchic", "Basic", "Torchic"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=255,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Fireworks",
            game_text="Flip a coin. If tails, discard a Fire Energy card attached to Torchic.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)