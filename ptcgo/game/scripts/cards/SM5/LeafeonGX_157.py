from ptcgo.game.card_effects.attacks_common import evolve_each_from_deck
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="565671d3-3907-5208-ae80-9c69b33e70f6",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonGX.Name",
    display_name="Leafeon-GX",
    searchable_by=["Leafeon-GX", "Stage 1", "GX", "LeafeonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=157,
    set_code="SM5",
    rarity=Rarities.RareRainbow,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Breath of the Leaves",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon, once during your turn (before your attack), you may heal 50 damage from 1 of your Pok\u00e9mon that has any Energy attached to it.",
            effect=unimplemented,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
        Attack(
            title="Grand Bloom-GX",
            game_text="For each of your Benched Basic Pok\u00e9mon, search your deck for a card that evolves from that Pok\u00e9mon and put it onto that Pok\u00e9mon to evolve it. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            effect=evolve_each_from_deck(target_pred=is_basic_pokemon),
        ),
    ],
)
