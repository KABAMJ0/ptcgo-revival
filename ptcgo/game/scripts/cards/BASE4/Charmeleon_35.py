from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="771490ce-618e-55cb-b239-42d8c3ce1ce8",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    display_name="Charmeleon",
    searchable_by=["Charmeleon", "Stage 1", "Charmeleon"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard 1 Fire Energy card attached to Charmeleon in order to use this attack.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)