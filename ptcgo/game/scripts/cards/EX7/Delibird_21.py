from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2e38d6e3-809c-5a11-b35b-26cbbf33bf82",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name",
    display_name="Delibird",
    searchable_by=["Delibird", "Basic", "Delibird"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="EX7",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=225,
    abilities=[
        Ability(
            title="Gift Exchange",
            game_text="Once during your turn (before your attack), if Delibird is your Active Pok\u00e9mon, you may shuffle 1 card from your hand into your deck. Then, draw a card. This power can't be used if Delibird is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Souvenir",
            game_text="Flip 3 coins. If 1 of them is heads, put 4 damage counters on the Defending Pok\u00e9mon. If 2 of them are heads, remove 1 damage counter from the Defending Pok\u00e9mon. If all of them are heads, put 10 damage counters on the Defending Pok\u00e9mon. If all of them are tails, remove all damage counters from the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)