from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack

card = PokemonCardDef(
    guid="30e6fb46-6a31-5df4-9c1a-624e334d316d",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latiasex.Name",
    display_name="Latias ex",
    searchable_by=["Latias ex", "Basic", "ex", "Latiasex"],
    subtypes=["Basic", "ex"],
    collector_number=220,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=380,
    abilities=[
        Ability(
            title="Skyliner",
            game_text="Your Basic Pok\u00e9mon in play have no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Eon Blade",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=lock_self_attack(),
        ),
    ],
)