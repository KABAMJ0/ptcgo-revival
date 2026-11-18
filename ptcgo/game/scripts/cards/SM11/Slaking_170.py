from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b9384b9c-f37a-5d32-be9a-a156fc93654d",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name",
    display_name="Slaking",
    searchable_by=["Slaking", "Stage 2", "Slaking"],
    subtypes=["Stage 2"],
    collector_number=170,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Counterattack",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), put 4 damage counters on the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Dynamic Swing",
            game_text="You may do 100 more damage. If you do, during your opponent's next turn, this Pok\u00e9mon takes 100 more damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)