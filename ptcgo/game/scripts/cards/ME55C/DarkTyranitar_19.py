from ptcgo.game.card_effects.attacks_common import damage_all_opponents
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_EX
from ptcgo.game.card_effects.attacks_common import bonus_if

card = PokemonCardDef(
    guid="55f5dd21-3001-5361-9710-2ee282aa4ac8",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkTyranitar.Name",
    display_name="Dark Tyranitar",
    searchable_by=["Dark Tyranitar", "Stage 2", "DarkTyranitar"],
    subtypes=["Stage 2"],
    collector_number=19,
    set_code="ME55C",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPupitar.Name",
    family_id=248,
    abilities=[
        Attack(
            title="Grind",
            game_text="Does 10 damage plus 10 more damage for each Energy attached to Dark Tyranitar.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Spinning Tail",
            game_text="Does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            effect=damage_all_opponents(20),
        ),
        Attack(
            title="Bite Off",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 70 damage plus 50 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=bonus_if(lambda ctx: is_pokemon_EX(ctx.defender), 50, base=70),
        ),
    ],
)