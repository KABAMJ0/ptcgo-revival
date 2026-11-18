from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5e1f0a43-a97b-5238-be02-4bacbc43fa77",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGardevoirEX.Name",
    display_name="M Gardevoir-EX",
    searchable_by=["M Gardevoir-EX", "MEGA", "EX", "MGardevoirEX"],
    subtypes=["MEGA", "EX"],
    collector_number=10031,
    set_code="TwentiethAnn",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirEX.Name",
    family_id=282,
    abilities=[
        Attack(
            title="Brilliant Arrow",
            game_text="This attack does 30 damage times the amount of Fairy Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)