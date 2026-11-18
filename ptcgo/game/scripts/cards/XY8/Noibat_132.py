from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_discard_opponent_energy

card = PokemonCardDef(
    guid="61585493-b07d-54d0-9b6f-cc302bb2b88b",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    display_name="Noibat",
    searchable_by=["Noibat", "Basic", "Noibat"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=714,
    abilities=[
        Attack(
            title="Mysterious Beam",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_discard_opponent_energy(),
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)