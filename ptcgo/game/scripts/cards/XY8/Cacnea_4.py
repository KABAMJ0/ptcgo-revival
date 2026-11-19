from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_discard_opponent_energy

card = PokemonCardDef(
    guid="60a98c57-1fdf-51ec-84f3-0011b3e9fa49",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    display_name="Cacnea",
    searchable_by=["Cacnea", "Basic", "Cacnea"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=331,
    abilities=[
        Attack(
            title="Swagger",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=flip_discard_opponent_energy(),
        ),
    ],
)