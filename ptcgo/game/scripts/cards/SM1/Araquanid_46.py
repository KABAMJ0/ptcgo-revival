from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="36d32820-0b3e-50f0-b9a1-140e2c83f41f",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Araquanid.Name",
    display_name="Araquanid",
    searchable_by=["Araquanid", "Stage 1", "Araquanid"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name",
    family_id=751,
    abilities=[
        Ability(
            title="Water Bubble",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Fire Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Aqua Edge",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)