from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="948404e8-9a92-589d-8056-03202ec63e84",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGreninjaex.Name",
    display_name="Mega Greninja ex",
    searchable_by=["Mega Greninja ex", "Stage 2", "MEGA", "ex", "MegaGreninjaex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=22,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=350,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=656,
    abilities=[
        Ability(
            title="Mortal Shuriken",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may discard a Basic Water Energy card from your hand in order to use this Ability. Place 6 damage counters on 1 of your opponent's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Ninja Spinner",
            game_text="You may put a Water Energy attached to this Pok\u00e9mon into your hand and have this attack do 80 more damage.",
            cost={PokemonTypes.WATER: 2},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)