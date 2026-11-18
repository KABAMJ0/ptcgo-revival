from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f3eed27a-3264-5916-a177-97c5a2260566",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1", "Delcatty"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Ability(
            title="Power Circulation",
            game_text="Once during your turn (before your attack), you may search your discard pile for up to 2 basic Energy cards, show them to your opponent, and put those cards on top of your deck in any order. If you do, put 2 damage counters on Delcatty. This power can't be used if Delcatty is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Power Heal",
            game_text="Does 10 damage plus 10 more damage for each damage counter on Delcatty. Then, remove 2 damage counters from Delcatty.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)