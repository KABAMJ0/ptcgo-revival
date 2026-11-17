from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aa8541f0-624e-5d2d-9220-b6289084dd6f",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name",
    display_name="Shuckle",
    searchable_by=["Shuckle", "Basic", "Shuckle"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=213,
    abilities=[
        Ability(
            title="Fermented Juice",
            game_text="Once during your turn, if this Pok\u00e9mon has any Grass Energy attached, you may use this Ability. Heal 30 damage from 1 of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)