from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="84053c1f-d5ef-5d15-b0e4-e2dfd244bfc9",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dachsbunex.Name",
    display_name="Dachsbun ex",
    searchable_by=["Dachsbun ex", "Stage 1", "ex", "Dachsbunex"],
    subtypes=["Stage 1", "ex"],
    collector_number=67,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fidough.Name",
    family_id=926,
    abilities=[
        Ability(
            title="Time to Chow Down",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may heal all damage from each of your Evolution Pok\u00e9mon. If you healed any damage in this way, discard all Energy from those Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Wonder Shine",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)