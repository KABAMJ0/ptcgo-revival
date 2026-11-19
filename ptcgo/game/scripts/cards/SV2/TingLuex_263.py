from ptcgo.game.card_effects.attacks_common import bench_counter_picks
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a8e2e335-c641-553c-962f-705cfbe753a7",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TingLuex.Name",
    display_name="Ting-Lu ex",
    searchable_by=["Ting-Lu ex", "Basic", "ex", "TingLuex"],
    subtypes=["Basic", "ex"],
    collector_number=263,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=240,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=1003,
    abilities=[
        Ability(
            title="Cursed Land",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Pok\u00e9mon in play that have any damage counters on them have no Abilities, except for Pok\u00e9mon ex.",
            effect=bench_counter_picks(1, 2),
        ),
        Attack(
            title="Land Scoop",
            game_text="Put 2 damage counters on 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=150,
            effect=bench_counter_picks(1, 2),
        ),
    ],
)