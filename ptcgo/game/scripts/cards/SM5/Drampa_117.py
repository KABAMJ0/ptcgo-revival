from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per, mill_attack
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="68cbe2c5-02a3-509f-a036-e9588c38366d",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drampa.Name",
    display_name="Drampa",
    searchable_by=["Drampa", "Basic", "Drampa"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="SM5",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=780,
    abilities=[
        Attack(
            title="Outrage",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), per=10, base=20),
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=mill_attack(count=2, opponent=False),
        ),
    ],
)