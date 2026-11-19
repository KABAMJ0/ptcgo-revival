from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f1de93cd-9797-56cd-b7dc-b735de839287",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsHitmonchanex.Name",
    display_name="Rocket's Hitmonchan ex",
    searchable_by=["Rocket's Hitmonchan ex", "Basic", "ex", "RocketsHitmonchanex"],
    subtypes=["Basic", "ex"],
    collector_number=98,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=107,
    abilities=[
        Ability(
            title="Strikes Back",
            game_text="If Rocket's Hitmonchan ex is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Rocket's Hitmonchan ex is Knocked Out), put 2 damage counters on the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Mach Punch",
            game_text="Does 10 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Magnum Punch",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)