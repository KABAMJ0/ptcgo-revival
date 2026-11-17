from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aa30bd38-ff90-5f27-b69b-91db8a5ca56b",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlazikenFB.Name",
    display_name="Blaziken FB",
    searchable_by=["Blaziken FB", "Basic", "SP", "BlazikenFB"],
    subtypes=["Basic", "SP"],
    collector_number=2,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=257,
    abilities=[
        Attack(
            title="Luring Flame",
            game_text="Switch the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon. The new Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Vapor Kick",
            game_text="If your opponent has any Water Pok\u00e9mon in play, this attack does 30 damage plus 30 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)