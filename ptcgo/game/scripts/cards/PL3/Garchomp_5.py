from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="33b7f682-53f0-500d-9469-53f1369f9841",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name",
    display_name="Garchomp",
    searchable_by=["Garchomp", "Stage 2", "Garchomp"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    family_id=443,
    abilities=[
        Ability(
            title="Dragon Intimidation",
            game_text="If Garchomp is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Garchomp is Knocked Out), choose an Energy card attached to the Attacking Pok\u00e9mon and put it into your opponent's hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Guard Claw",
            game_text="During your opponent's next turn, any damage done to Garchomp by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Speed Impact",
            game_text="Does 120 damage minus 20 damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)