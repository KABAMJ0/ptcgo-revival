from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import def_for


def _antique_on_bench(ctx) -> int:
    return sum(1 for pokemon in ctx.my_bench()
               if "antique" in (getattr(def_for(pokemon.archetype_id),
                                       "display_name", "") or "").lower())


card = PokemonCardDef(
    guid="79ba2e58-5e5d-512e-b615-c2d9b0b62988",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Relicanth.Name",
    display_name="Relicanth",
    searchable_by=["Relicanth", "Basic", "Relicanth"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=369,
    abilities=[
        Attack(
            title="Fossil Beatdown",
            game_text="This attack does 30 more damage for each of your Benched Pok\u00e9mon that has \"Antique\" in its name.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(_antique_on_bench, 30, base=10),
        ),
    ],
)