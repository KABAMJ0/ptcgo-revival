from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack

card = PokemonCardDef(
    guid="bd25d3fc-377b-5ca4-a3dc-4e8ddc33cacf",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name",
    display_name="Magmortar",
    searchable_by=["Magmortar", "Stage 1", "Magmortar"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    family_id=126,
    abilities=[
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
        ),
        Attack(
            title="Volcanic Heat",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=lock_self_attack(),
        ),
    ],
)