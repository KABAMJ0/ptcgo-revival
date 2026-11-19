from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_EX
from ptcgo.game.card_effects.attacks_common import bonus_if

card = PokemonCardDef(
    guid="07dcc8d7-4fd5-5ce9-89e1-e7fff55b9c1f",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra δ",
    searchable_by=["Kingdra \u03b4", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=230,
    abilities=[
        Ability(
            title="Dragon Curse",
            game_text="Once during your turn (before your attack), if Kingdra is your Active Pok\u00e9mon, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon with \u03b4 on its card. This power can't be used if Kingdra is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Extra Flame",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 30 damage plus 30 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(lambda ctx: is_pokemon_EX(ctx.defender), 30, base=30),
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)