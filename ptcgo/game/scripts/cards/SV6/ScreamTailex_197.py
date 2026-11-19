from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack

card = PokemonCardDef(
    guid="c1bfd0df-7cff-5415-9d67-fc0481eee850",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScreamTailex.Name",
    display_name="Scream Tail ex",
    searchable_by=["Scream Tail ex", "Basic", "ex", "Ancient", "ScreamTailex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=197,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=985,
    abilities=[
        Attack(
            title="Scream",
            game_text="You can use this attack only if you go second, and only during your first turn. Your opponent can't play any Supporter cards from their hand during their next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Crunch",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=discard_opponent_energy_attack(1),
        ),
    ],
)