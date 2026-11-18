from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import no_retreat_passive, opposing_active, is_in_active_spot

card = PokemonCardDef(
    guid="9391f1fb-f06e-593c-a694-559cbcbe2734",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Team Plasma", "Snorlax"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=101,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Block",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent's Active Pok\u00e9mon can't retreat.",
            passive=no_retreat_passive(lambda p, c: opposing_active(p, c) and is_in_active_spot(c)),
        ),
        Attack(
            title="Teampact",
            game_text="Does 30 damage times the number of Team Plasma Pok\u00e9mon you have in play.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)