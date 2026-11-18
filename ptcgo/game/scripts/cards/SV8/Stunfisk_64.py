from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_discard_opponent_energy

card = PokemonCardDef(
    guid="8e092d64-72e4-5555-b81a-6ee0b823d9c6",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunfisk.Name",
    display_name="Stunfisk",
    searchable_by=["Stunfisk", "Basic", "Stunfisk"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=618,
    abilities=[
        Attack(
            title="Paralyzing Crackle",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed, and discard an Energy from that Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=flip_discard_opponent_energy(),
        ),
    ],
)