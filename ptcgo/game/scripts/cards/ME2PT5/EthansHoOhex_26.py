from ptcgo.game.card_effects.support_common import heal_targets
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="02c95fdc-384b-5d8e-8daa-1de594964e4f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansHoOhex.Name",
    display_name="Ethan's Ho-Oh ex",
    searchable_by=["Ethan's Ho-Oh ex", "Basic", "ex", "EthansHoOhex"],
    subtypes=["Basic", "ex"],
    collector_number=26,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=250,
    abilities=[
        Ability(
            title="Golden Flame",
            game_text="Once during your turn, you may attach up to 2 Basic Fire Energy cards from your hand to 1 of your Benched Ethan's Pok\u00e9mon.",
            effect=heal_targets(50, scope="each_own"),
        ),
        Attack(
            title="Shining Feathers",
            game_text="Heal 50 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 4},
            damage=160,
            effect=unimplemented,
        ),
    ],
)