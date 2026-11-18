from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8a226859-5298-5828-831a-66e4dbccc76c",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name",
    display_name="Abomasnow",
    searchable_by=["Abomasnow", "Stage 1", "Abomasnow"],
    subtypes=["Stage 1"],
    collector_number=101,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    family_id=459,
    abilities=[
        Ability(
            title="Freezing Disaster",
            game_text="Pok\u00e9mon (both yours and your opponent's) can't be healed.",
            effect=unimplemented,
        ),
        Attack(
            title="Magnum Punch",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)