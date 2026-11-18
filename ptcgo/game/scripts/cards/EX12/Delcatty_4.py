from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ccca713f-efd7-5b39-bf8d-a7344a0ec867",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1", "Delcatty"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="EX12",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Ability(
            title="Reactive Shift",
            game_text="Once during your turn (before your attack), you may move a React Energy card attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon. This power can't be used if Delcatty is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Link",
            game_text="Search your discard pile for an Energy card and attach it to Delcatty.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)