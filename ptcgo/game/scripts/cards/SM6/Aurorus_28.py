from ptcgo.game.card_effects.passives_common import protect_next_turn, attacker_is_basic, attacker_is_evolution
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c66198bb-0758-5ea0-88e1-5a44c749b9f6",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aurorus.Name",
    display_name="Aurorus",
    searchable_by=["Aurorus", "Stage 2", "Aurorus"],
    subtypes=["Stage 2"],
    collector_number=28,
    set_code="SM6",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Amaura.Name",
    family_id=698,
    abilities=[
        Attack(
            title="Frost Wall",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Evolution Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=protect_next_turn(prevent=True, attacker_pred=attacker_is_evolution()),
        ),
        Attack(
            title="Blizzard Burn",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=unimplemented,
        ),
    ],
)