from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_evolution_pokemon
from ptcgo.game.card_effects.attacks_common import bonus_if

card = PokemonCardDef(
    guid="91628e74-d45c-5243-aec9-b6bfea8f114b",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill δ",
    searchable_by=["Beedrill \u03b4", "Stage 2", "Beedrill"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Ability(
            title="Final Sting",
            game_text="Once during your turn (before your attack), you may Knock Out Beedrill. If you do, choose 1 of your opponent's Defending Pok\u00e9mon. That Pok\u00e9mon is now Paralyzed and Poisoned. Put 2 damage counters instead of 1 on that Pok\u00e9mon between turns. This power can't be used if Beedrill is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Super Slash",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, this attack does 50 damage plus 30 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=bonus_if(lambda ctx: is_evolution_pokemon(ctx.defender), 30),
        ),
    ],
)