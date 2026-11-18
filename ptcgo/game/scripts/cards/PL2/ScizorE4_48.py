from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ae7dae1f-5a9e-546b-863d-b9f95ba1cc5e",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScizorE4.Name",
    display_name="Scizor E4",
    searchable_by=["Scizor E4", "Basic", "SP", "ScizorE4"],
    subtypes=["Basic", "SP"],
    collector_number=48,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=212,
    abilities=[
        Attack(
            title="Cut",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Crushing Blow",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=composed(lambda ctx: ctx.deal_damage(), flip_gate(then=discard_opponent_energy_attack(1, damage=0))),
        ),
    ],
)