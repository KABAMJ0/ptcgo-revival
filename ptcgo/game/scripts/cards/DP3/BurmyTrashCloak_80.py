from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3972b272-38fa-5e8d-abfb-7eee035747cf",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BurmyTrashCloak.Name",
    display_name="Burmy Trash Cloak",
    searchable_by=["Burmy Trash Cloak", "Basic", "BurmyTrashCloak"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=412,
    abilities=[
        Ability(
            title="Wear Cloak",
            game_text="Once during your turn (before your attack), if Burmy Trash Cloak is your Active Pok\u00e9mon, you may search your discard for a basic Metal Energy card and attach it to Burmy Trash Cloak.",
            effect=unimplemented,
        ),
        Attack(
            title="Trash Cloak Tackle",
            game_text="If Burmy Trash Cloak has any Metal Energy attached to it, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)