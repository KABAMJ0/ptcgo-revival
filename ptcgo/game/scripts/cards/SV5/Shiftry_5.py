from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import return_attached_energy

card = PokemonCardDef(
    guid="aa1e211b-cf68-53bc-9921-16d2f140381c",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Expelling Tornado",
            game_text="Choose 3 of your opponent's Benched Pok\u00e9mon. If you do, shuffle all of your opponent's Benched Pok\u00e9mon that you didn't choose, and all cards attached to those Pok\u00e9mon, into their deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Energy Loop",
            game_text="Put an Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=return_attached_energy(count=1, to="hand", target="self"),
        ),
    ],
)