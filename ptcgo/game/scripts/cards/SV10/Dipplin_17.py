from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.support_common import return_attached_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="14f1fad7-ae60-5170-82cf-a700de50ca7a",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dipplin.Name",
    display_name="Dipplin",
    searchable_by=["Dipplin", "Stage 1", "Dipplin"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Attack(
            title="Energy Loop",
            game_text="Put an Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=composed(lambda ctx: ctx.deal_damage(), return_attached_energy(count=1)),
        ),
    ],
)