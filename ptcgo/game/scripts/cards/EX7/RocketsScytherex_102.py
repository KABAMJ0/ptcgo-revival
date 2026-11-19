from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ee3550f6-631f-5a79-ae48-ef507030d188",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsScytherex.Name",
    display_name="Rocket's Scyther ex",
    searchable_by=["Rocket's Scyther ex", "Basic", "ex", "RocketsScytherex"],
    subtypes=["Basic", "ex"],
    collector_number=102,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=123,
    abilities=[
        Ability(
            title="Dual Armor",
            game_text="As long as Rocket's Scyther ex has any Grass Energy attached to it, Rocket's Scyther ex is both Grass and Darkness type.",
            effect=unimplemented,
        ),
        Attack(
            title="Bounce",
            game_text="After your attack, you may switch Rocket's Scyther ex with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Slashing Strike",
            game_text="Rocket's Scyther ex can't use Slashing Strike during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=unimplemented,
        ),
    ],
)