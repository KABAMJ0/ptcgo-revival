from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f47a07a1-cafc-502b-a09e-3b3c36d1ca34",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name",
    display_name="Crocalor",
    searchable_by=["Crocalor", "Stage 1", "Crocalor"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name",
    family_id=909,
    abilities=[
        Attack(
            title="Rolling Fireball",
            game_text="Put an Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.FIRE: 2},
            damage=90,
            effect=unimplemented,
        ),
    ],
)