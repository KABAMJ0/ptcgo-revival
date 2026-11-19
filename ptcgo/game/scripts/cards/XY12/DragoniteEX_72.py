from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack

card = PokemonCardDef(
    guid="f930d96c-dfdf-585a-bb06-893922f476e8",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteEX.Name",
    display_name="Dragonite-EX",
    searchable_by=["Dragonite-EX", "Basic", "EX", "DragoniteEX"],
    subtypes=["Basic", "EX"],
    collector_number=72,
    set_code="XY12",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=149,
    abilities=[
        Ability(
            title="Pull Up",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may put 2 Basic Pok\u00e9mon (except for Dragonite-EX) from your discard pile into your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Hyper Beam",
            game_text="Discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            effect=discard_opponent_energy_attack(1),
        ),
    ],
)