from ptcgo.game.card_effects.passives_common import composed, protect_next_turn
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e739f37e-a495-568a-9ba2-04a6adbc0982",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon", "Stage 2", "Empoleon"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="DP7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=395,
    abilities=[
        Ability(
            title="Emperor Aura",
            game_text="Once during your turn (before your attack), when you play Empoleon from your hand to evolve 1 of your Active Pok\u00e9mon, you may use this power. Your opponent can't attach any Energy cards from his or her hand to his or her Pok\u00e9mon during your opponent's next turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, any damage done to Empoleon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Whirlpool",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=composed(lambda ctx: ctx.deal_damage(), flip_gate(then=discard_opponent_energy_attack(1, damage=0))),
        ),
    ],
)