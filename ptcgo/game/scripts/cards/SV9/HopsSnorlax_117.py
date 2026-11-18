from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="43304079-4772-5728-977c-8b1d78dd81c9",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsSnorlax.Name",
    display_name="Hop's Snorlax",
    searchable_by=["Hop's Snorlax", "Basic", "HopsSnorlax"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Extra Helpings",
            game_text="Attacks used by your Hop's Pok\u00e9mon do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance). The effect of Extra Helpings doesn't stack.",
            effect=unimplemented,
        ),
        Attack(
            title="Dynamic Press",
            game_text="This Pok\u00e9mon also does 80 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
            effect=unimplemented,
        ),
    ],
)