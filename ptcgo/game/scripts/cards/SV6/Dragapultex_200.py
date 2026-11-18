from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import phantom_dive

card = PokemonCardDef(
    guid="9c6ef206-111a-520c-960b-b916b1d95125",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragapultex.Name",
    display_name="Dragapult ex",
    searchable_by=["Dragapult ex", "Stage 2", "Tera", "ex", "Dragapultex"],
    subtypes=["Stage 2", "Tera", "ex"],
    collector_number=200,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name",
    family_id=885,
    abilities=[
        Attack(
            title="Jet Headbutt",
            cost={PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
        Attack(
            title="Phantom Dive",
            game_text="Put 6 damage counters on your opponent's Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1},
            damage=200,
            effect=phantom_dive,
        ),
    ],
)