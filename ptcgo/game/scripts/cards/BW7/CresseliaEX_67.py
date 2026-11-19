from ptcgo.game.card_effects.attacks_common import no_weakness_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_weakness_next_turn

card = PokemonCardDef(
    guid="7a8f0d65-24aa-5f15-96a2-fe117315e466",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CresseliaEX.Name",
    display_name="Cresselia-EX",
    searchable_by=["Cresselia-EX", "Basic", "EX", "CresseliaEX"],
    subtypes=["Basic", "EX"],
    collector_number=67,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=488,
    abilities=[
        Ability(
            title="Sparkling Particles",
            game_text="At any time between turns, heal 10 damage from this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Protection",
            game_text="During your opponent's next turn, this Pok\u00e9mon has no Weakness.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=no_weakness_next_turn(),
        ),
    ],
)