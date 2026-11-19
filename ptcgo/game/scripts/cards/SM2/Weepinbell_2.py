from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2b9fda36-e326-5a80-8774-25b8fc420064",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    display_name="Weepinbell",
    searchable_by=["Weepinbell", "Stage 1", "Weepinbell"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Muddy Acid",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=flip_gate(discard_opponent_energy_attack(1)),
        ),
    ],
)