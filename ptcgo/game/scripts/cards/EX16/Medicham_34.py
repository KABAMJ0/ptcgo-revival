from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="df331675-adc2-5694-8ef5-92a859c8bbd0",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name="Medicham",
    searchable_by=["Medicham", "Stage 1", "Medicham"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Ability(
            title="Vigorous Aura",
            game_text="As long as Medicham is your Active Pok\u00e9mon, attacks by each player's Active Pok\u00e9mon do 10 more damage to any Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Punch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Rolling Kick",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)