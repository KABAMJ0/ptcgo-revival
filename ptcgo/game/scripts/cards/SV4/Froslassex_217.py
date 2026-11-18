from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a0143a0a-400d-5f88-bdbf-bfb364251bee",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froslassex.Name",
    display_name="Froslass ex",
    searchable_by=["Froslass ex", "Stage 1", "Tera", "ex", "Froslassex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=217,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=250,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Ability(
            title="Evanescent",
            game_text="If this Pok\u00e9mon is in the Active Spot and is Knocked Out, flip a coin. If heads, your opponent takes 1 fewer Prize card.",
            effect=unimplemented,
        ),
        Attack(
            title="Frost Bullet",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2},
            damage=140,
            effect=unimplemented,
        ),
    ],
)